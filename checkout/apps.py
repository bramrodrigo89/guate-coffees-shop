from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        
        Override ready method to import signals module: every time
        a line item is saved/deleted, order toal will be updated
        """
        import checkout.signals
