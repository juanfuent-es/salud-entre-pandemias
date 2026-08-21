#!/usr/bin/env python3

import argparse
from pathlib import Path

import yt_dlp


def descargar_subtitulos(url: str, destino: str, idiomas: list[str]) -> None:
    carpeta = Path(destino)
    carpeta.mkdir(parents=True, exist_ok=True)

    opciones = {
        # No descargar audio ni video
        "skip_download": True,

        # Descargar subtítulos creados por el autor
        "writesubtitles": True,

        # Descargar subtítulos automáticos de YouTube
        "writeautomaticsub": True,

        # Idiomas solicitados
        "subtitleslangs": idiomas,

        # Usar el mejor formato disponible
        "subtitlesformat": "best",

        # Convertir los subtítulos a SRT mediante FFmpeg
        "convertsubtitles": "srt",

        # Procesar videos, playlists y canales completos
        "yes_playlist": True,

        # Continuar aunque algún video falle o no tenga subtítulos
        "ignoreerrors": True,

        # Evitar sobrescribir archivos existentes
        "overwrites": False,

        # Organización de archivos
        "outtmpl": str(
            carpeta
            / "%(uploader)s"
            / "%(playlist_title,playlist|Videos)s"
            / "%(playlist_index,autonumber)04d - %(title)s [%(id)s].%(ext)s"
        ),
    }

    print(f"Procesando: {url}")
    print(f"Destino: {carpeta.resolve()}")
    print(f"Idiomas: {', '.join(idiomas)}")

    with yt_dlp.YoutubeDL(opciones) as ydl:
        codigo = ydl.download([url])

    if codigo == 0:
        print("\nProceso terminado.")
    else:
        print("\nEl proceso terminó con algunos errores.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Descarga subtítulos de videos, playlists o canales de YouTube."
    )

    parser.add_argument(
        "url",
        help="URL del video, playlist o canal de YouTube",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="subtitulos",
        help="Carpeta de destino. Predeterminada: subtitulos",
    )

    parser.add_argument(
        "-l",
        "--langs",
        default="es.*,en.*",
        help='Idiomas separados por comas. Usa "all" para todos.',
    )

    argumentos = parser.parse_args()

    idiomas = [
        idioma.strip()
        for idioma in argumentos.langs.split(",")
        if idioma.strip()
    ]

    descargar_subtitulos(
        url=argumentos.url,
        destino=argumentos.output,
        idiomas=idiomas,
    )


if __name__ == "__main__":
    main()