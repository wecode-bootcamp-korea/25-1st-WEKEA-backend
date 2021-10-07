from django.db import models

class Order(models.Model):
    order_number     = models.CharField(max_length = 100)
    user             = models.ForeignKey('user.User', on_delete = models.CASCADE, related_name = 'orders')
    order_state_code = models.ForeignKey('OrderStatus', on_delete = models.CASCADE, related_name = 'order_statuses')
    order_details    = models.CharField(max_length = 20)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return '%s %s' % (self.user, self.order_details)

class OrderStatus(models.Model):
    order_status_description = models.CharField(max_length = 20)

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return self.order_status_description

class Shipment(models.Model):
    shipment_tracking_number = models.IntegerField()
    other_shipment_details   = models.CharField(max_length = 20)
    order                    = models.ForeignKey('Order', on_delete = models.CASCADE, related_name = 'shipments')
    
    class Meta:
        db_table = 'shipments'
    
    def __str__(self):
        return '%s %s' % (self.shipment_tracking_number, self.other_shipment_details)

class OrderItem(models.Model):
    order                    = models.ForeignKey('Order', on_delete = models.CASCADE, related_name = 'order_items')
    product                  = models.ForeignKey('product.Product', on_delete = models.CASCADE, related_name = 'order_items')
    order_item_status        = models.ForeignKey('OrderItemStatus', on_delete = models.CASCADE, related_name = 'order_items')
    order_item_quantity      = models.DecimalField(max_digits = 10, decimal_places = 2)
    order_item_price         = models.DecimalField(max_digits = 10, decimal_places = 2)
    RMA_number               = models.IntegerField(null = True)
    RMA_issued_by            = models.BooleanField(default = False)
    RMA_issued_date          = models.DateTimeField(null = True)
    other_order_item_details = models.CharField(max_length = 50, blank = True)

    class Meta:
        db_table = 'order_items'
    def __str__(self):
        return '%s %s %s' % (self.order, self.order_item_quantity, self.order_item_price)

class OrderItemStatus(models.Model):
    order_item_status = models.CharField(max_length = 20)

    class Meta:
        db_table = 'order_item_statuses'

    def __str__(self):
        return self.order_item_status

class ShipmentItem(models.Model):
    order_item = models.ForeignKey('OrderItem', on_delete = models.CASCADE, related_name = 'shipment_items')
    shipment   = models.ForeignKey('Shipment', on_delete = models.CASCADE, related_name = 'shipment_items')
    
    class Meta:
        db_table = 'shipment_items'
    
    def __str__(self):
        return '%s %s' % (self.order_item, self.shipment)
