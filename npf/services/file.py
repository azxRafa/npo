import aiofiles
import pickle
from uuid import uuid4
from functools import lru_cache

import pandas as pd
from fastapi import Depends, UploadFile, File, HTTPException, status


class FileService:
    def __init__(self, file: UploadFile):
        self.file = file

    async def get_metrix(self) -> str:
        if self.file.content_type != "text/csv":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Error content type'
            )

        out_file_path = f"media/{uuid4()}.csv"
        async with aiofiles.open(out_file_path, 'wb') as out_file:
            while content := await self.file.read(1024):
                await out_file.write(content)

        train = pd.read_csv(out_file_path)
        with open('model/model.pickle', 'rb') as f:
            model = pickle.load(f)

        train = train.drop(
            [
                'lst_pmnt_date_per_qrtr',
                'slctn_nmbr',
                'client_id',
                'postal_code',
                'assignee_ops',
                'assignee_npo',
                'lk',
                'appl_mrkr'
            ],
            axis=1
        )

        train[[
            'email', 'phone_number', 'fact_addrss',
            'citizen', 'region', 'pmnts_type',
            'year', 'gender', 'age']
        ] = train[[
            'email', 'phone_number', 'fact_addrss',
            'citizen', 'region', 'pmnts_type',
            'year', 'gender', 'age'
        ]].astype('str')

        train = train.fillna('unknown')

        pred = model.predict(train)
        train['churn'] = pred

        out_file_path = f"media/{uuid4()}.csv"
        train[['npo_account_id',  'quarter',  'churn']].to_csv(out_file_path, index=0)

        return out_file_path


@lru_cache()
def get_file_service(
        file: UploadFile = File(...)
) -> FileService:
    return FileService(file)
