class Evento:
    def __init__(self, titulo, fecha_hora, duracion=1, descripcion= "", importancia= "normal", fecha_hora_recordatorio= None, etiquetas=None):
        self.titulo= titulo
        self.fecha_hora= fecha_hora
        self.duracion= duracion
        self.descripcion= descripcion
        self.importancia= importancia
        self.fecha_hora_recordatorio= fecha_hora_recordatorio
        self.etiquetas= etiquetas if etiquetas else []