// STRIPE - Accept one-time payments

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        fontFamily: 'Ubuntu Condensed, sans-serif',
        fontSmoothing: "antialiased",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        fontFamily: 'Ubuntu Condensed, sans-serif',
        color: "#b71c1c",
        iconColor: "#b71c1c"
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.on("change", function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
