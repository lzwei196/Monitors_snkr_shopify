from others.flask_sqlalchemy_db import db, snkrs
import json

class Nike:
    def __init__(self, current_status, region):
        self.current_status = current_status
        self.region = region

    def query_db(self):
        old_status = snkrs.query.filter_by(region=self.region).first()
        return old_status

    def current_status_with_availability(self):
        current_status_id_with_availability = {}
        for obj in self.current_status:
            if obj["productInfo"]:
                current_status_id_with_availability[obj["id"]] = obj["productInfo"][0]["availability"]["available"]
            else:
                current_status_id_with_availability[obj["id"]] = "N/A"

        return current_status_id_with_availability

    def current_status_ana(self):
        current_status_id =[]
        #retrieve the id of each obj in the list, to compare with the new status
        for obj in self.current_status:
            current_status_id.append(obj["id"])
        return current_status_id

    def update_db(self, old_status, current_status_ana):
        old_status.status = json.dumps(current_status_ana)
        db.session.commit()


