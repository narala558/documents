import razorpay

rc = razorpay.Client(
    auth=('', '')
)

amount = 100

data = {
    'amount': amount,
    'currency': 'USD',
    'receipt': '12',
    'payment_capture': 1,
}
rc.order.create(data)

x = rc.payment.capture('pay_7gALpwGaPwyanh', 5000)

# {'id': 'pay_7gALpwGaPwyanh', 'entity': 'payment', 'amount': 5000, 'currency': 'INR', 'base_amount': 5000, 'status': 'captured', 'order_id': None, 'invoice_id': None, 'international': False, 'method': 'upi', 'amount_refunded': 0, 'amount_paidout': 0, 'refund_status': None, 'captured': True, 'description': 'Purchase Description', 'card_id': None, 'bank': None, 'wallet': None, 'vpa': 'iii@icici', 'email': 'support@razorpay.com', 'contact': '888888888888888', 'notes': [], 'fee': 115, 'service_tax': 15, 'error_code': None, 'error_description': None, 'created_at': 1492500747} aaaa


print(x, 'aaaa')
print('do')
