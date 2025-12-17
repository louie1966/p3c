@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers