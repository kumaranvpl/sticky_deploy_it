from fastagency import FastAgency
from fastagency.ui.mesop import MesopUI

from ..workflow import wf

app = FastAgency(
    provider=wf,
    ui=MesopUI(),
    title="Sticky Deploy It",
)

# start the fastagency app with the following command
# gunicorn sticky_deploy_it.local.main_mesop:app
