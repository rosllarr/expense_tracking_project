### Create simple data on Month table.
```bash
# reset model id
python manage.py sqlsequencereset month

# create transections data for June and May 
python manage.py generate_simple_data june may
```