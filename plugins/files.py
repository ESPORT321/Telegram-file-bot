from database import files

async def save_file(file_id, file_name):
    await files.insert_one({
        "file_id": file_id,
        "file_name": file_name
    })

async def get_files():
    return await files.find().to_list(length=None)

async def delete_file(file_id):
    await files.delete_one({"file_id": file_id})
