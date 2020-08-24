// STRIPE - Accept one-time payments

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        fontFamily: 'Roboto, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        fontFamily: 'Roboto, sans-serif',
        color: "#b71c1c",
        iconColor: "#b71c1c"
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

card.on("change", function (event) {
    // Disable the Pay button if there are no card details in the Element
    document.querySelector("button").disabled = event.empty;
    document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
});