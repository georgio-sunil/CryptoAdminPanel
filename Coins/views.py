from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from services import api
from services.models.Coin import Coins
from utilities import validation_checks

class CoinTable(LoginRequiredMixin, TemplateView):
    template_name = "coins/coin-table.html"
    success_url = "coins/coin-table.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    coinData = api.fetchCMCCoins()

    def post(self, request, *args, **kwargs):

        # Add Coin from CMC API response
        if 'add-coin' in self.request.POST:
            api_coinData = self.coinData
            toSave = request.POST.getlist('addCoin')
            list_coins = api.fetchCoins()
            toSave = validation_checks.idNotInCoinList(toSave, list_coins)
            for id in toSave:
                for coin in api_coinData:
                    if (coin['id'] == int(id)):
                        logoUrl = "https://s2.coinmarketcap.com/static/img/coins/64x64/" + \
                            str(id) + ".png"
                        coinObject = Coins(id, coin['symbol'], coin['symbol'], logoUrl, True)
                        if api.addCoins(coinObject):
                            print("Coin added")

        # Disable the coin.
        elif 'disable-coin' in self.request.POST:
            toDisable = request.POST.getlist('disableCoin')
            for id in toDisable:
                if api.coinStatus(id, False):
                    print("Coin Disabled")

        # Enable the coin.
        elif 'enable-coin' in self.request.POST:
            toEnable = request.POST.getlist('disableCoin')
            for id in toEnable:
                if api.coinStatus(id, True):
                    print("Coin Enabled")
        
        elif 'add-coin-ranking' in self.request.POST:
            for key, value in request.POST.items():
                if key.isnumeric() and (value != ""):
                    if api.coinRanking(key, value):
                        print("Coin rank added")
                    else:
                        messages.error(self.request, "Coin rank addition unsuccessful.")
            messages.success(self.request,'Coin ranks for the selected coins added.')
            return HttpResponseRedirect(self.request.path_info)
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        list_coins = api.fetchCoins()
        context = {
            "data": self.coinData,
            "internal_coins": list_coins
        }
        return context

