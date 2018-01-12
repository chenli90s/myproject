


class Algo:


    def __init__(self, app, config):
        self.app = app()
        self.config = config()
        self.type = config.event_type

    def run(self, event):
        if event.type == self.config.event_type:
            params = event.params
            params.status = 'init'
            self.app.init(params)
            params.status = 'runing'
            result = self.app.run(self.config.get_data())
            params.status = 'done'
            self.config.process_result(result)
            self.app.destory(event)


