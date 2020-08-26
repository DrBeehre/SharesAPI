import HatchService
import SharesiesService
import SimplicityService
import asyncio

def get_values(email, password):
    return asyncio.run(get_portfolio_values(email, password))

async def get_portfolio_values(email, password):

    hatch_portfolio_value = asyncio.create_task(HatchService.get_hatch_portfolio_value(email, password))
    sharesies_portfolio_value = asyncio.create_task(SharesiesService.get_sharesies_portfolio_value(email, password))
    simplicity_portfolio_value = asyncio.create_task(SimplicityService.get_simplicity_portfolio_value(email, password))

    await hatch_portfolio_value
    await sharesies_portfolio_value
    await simplicity_portfolio_value

    print(hatch_portfolio_value)
    print(sharesies_portfolio_value)
    print(simplicity_portfolio_value)