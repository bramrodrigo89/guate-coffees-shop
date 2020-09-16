// HOw to Set value in country selector always selected
// $('option[value=US]').attr('selected',true);

// Make the county select required for checkout form
$('select[name="country"]').attr('required',true);
// STRIPE - Accept one-time payments

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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
            <span role="alert">
                <i class="material-icons left">error</i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

// Stripe Javascript to confirm credit card payment on form submit
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    // First disable card and submit button to avoid multiple form submits and activate the loading overlay
    card.update({ 'disabled': true });
    $('#checkout-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Cache data first that can't be saved in payment intent, and then confirm card payment
    var saveInfo = Boolean($('#save-info-box').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Object with necessary data to post in URL
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    // Post data in url and then confirm card payment when Http response is 200 from server side
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.last_name.value) + ', ' + $.trim(form.first_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address_1.value),
                        line2: $.trim(form.street_address_2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.state.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.last_name.value) + ', ' + $.trim(form.first_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address_1.value),
                    line2: $.trim(form.street_address_2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.state.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                // Show error to your customer (e.g., insufficient funds)
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span role="alert">
                        <i class="material-icons left">error</i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                $(errorDiv).html(html);
                // Enable form submit button for customer to correct mistakes
                card.update({ 'disabled': false });
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                $('#checkout-button').attr('disabled', false);
            } else {
                // The payment has been processed!
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page in case there is not a 200 Http response from server when posting data to URL
        location.reload();
    });
});