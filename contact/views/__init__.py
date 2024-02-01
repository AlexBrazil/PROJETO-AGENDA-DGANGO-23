# CUIDADO ao usar "import *" em todos os módulos, pois se existirem "def" com o mesmo nome, um substituirá o outro

from .contact_views import *
from .contact_forms import *
from .user_forms import *

# contacts = Contact.objects.all()
# for item in contacts:
#     print(item)