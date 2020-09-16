from model import Donation, Donor


# print([x for x in Donation.select().dicts()])
# print([x for x in Donation.select().dicts() if x['donor'] == 1])

print([x for x in Donor.select().dicts() if x['name'] == 'Alice'])

print([x['id'] for x in Donor.select().dicts() if x['name'] == 'Alice'])


query = Donor.select().where(Donor.name=='Alice')

for x in query:
    print('{}'.format(x.name))

# query = Donation.select().dicts()
# for x in query:
#     print(x['donor'])



# print(Donation.select().dicts())
# print(Donation.select().dicts())
# print(Donation.select()
# # Donation.value, Donation.donor


# for x in query:
#     for (y, z) in x.items():
#         print(z)
# zz = (
# Donation
# .select()
# .dicts()
# .join(Donor)
# )
# print(zz)
# Donor.select().where(Donor.name == request.form['name']).dicts()
