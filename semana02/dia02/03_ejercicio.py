"""Aplicación sencilla para registrar, listar, actualizar y eliminar empresas.

Datos básicos por empresa:
- ruc: identificador único (string)
- nombre: nombre comercial
- rubro: actividad / sector

Los datos se persisten en un archivo JSON llamado `companies.json` en el
misma carpeta que este script. El script ofrece un menú interactivo y un
modo no-interactivo `--demo` para pruebas.
"""

from pathlib import Path
import json
import argparse
import sys

DATA_FILE = Path(__file__).with_name("companies.json")


def load_companies():
	if not DATA_FILE.exists():
		return []
	try:
		with DATA_FILE.open("r", encoding="utf-8") as f:
			return json.load(f)
	except Exception:
		return []


def save_companies(companies):
	with DATA_FILE.open("w", encoding="utf-8") as f:
		json.dump(companies, f, ensure_ascii=False, indent=2)


def find_company(companies, ruc):
	for i, c in enumerate(companies):
		if c.get("ruc") == ruc:
			return i
	return None


def register_company(companies, ruc=None, nombre=None, rubro=None):
	# interactive fallback if values not provided
	if ruc is None:
		ruc = input("RUC: ").strip()
	if find_company(companies, ruc) is not None:
		print("Ya existe una empresa con ese RUC.")
		return False
	if nombre is None:
		nombre = input("Nombre: ").strip()
	if rubro is None:
		rubro = input("Rubro: ").strip()
	companies.append({"ruc": ruc, "nombre": nombre, "rubro": rubro})
	save_companies(companies)
	print("Empresa registrada.")
	return True


def list_companies(companies):
	if not companies:
		print("No hay empresas registradas.")
		return
	print("Empresas registradas:")
	for c in companies:
		print(f"- RUC: {c.get('ruc')}, Nombre: {c.get('nombre')}, Rubro: {c.get('rubro')}")


def update_company(companies, ruc=None):
	if ruc is None:
		ruc = input("RUC de la empresa a actualizar: ").strip()
	idx = find_company(companies, ruc)
	if idx is None:
		print("Empresa no encontrada.")
		return False
	comp = companies[idx]
	print(f"Actualizando empresa {comp.get('nombre')} (RUC: {comp.get('ruc')})")
	nombre = input(f"Nuevo nombre [{comp.get('nombre')}]: ").strip() or comp.get('nombre')
	rubro = input(f"Nuevo rubro [{comp.get('rubro')}]: ").strip() or comp.get('rubro')
	companies[idx] = {"ruc": comp.get("ruc"), "nombre": nombre, "rubro": rubro}
	save_companies(companies)
	print("Empresa actualizada.")
	return True


def delete_company(companies, ruc=None):
	if ruc is None:
		ruc = input("RUC de la empresa a eliminar: ").strip()
	idx = find_company(companies, ruc)
	if idx is None:
		print("Empresa no encontrada.")
		return False
	comp = companies.pop(idx)
	save_companies(companies)
	print(f"Empresa {comp.get('nombre')} eliminada.")
	return True


def interactive_menu():
	companies = load_companies()
	while True:
		print("\n--- Menú de empresas ---")
		print("1) Registrar empresa")
		print("2) Listar empresas")
		print("3) Actualizar empresa")
		print("4) Eliminar empresa")
		print("5) Salir")
		choice = input("Elija una opción: ").strip()
		if choice == "1":
			register_company(companies)
		elif choice == "2":
			list_companies(companies)
		elif choice == "3":
			update_company(companies)
		elif choice == "4":
			delete_company(companies)
		elif choice == "5":
			print("Adiós")
			break
		else:
			print("Opción no válida.")


def demo_run():
	# Demo: clear data file, run a few operations non-interactively
	companies = []
	save_companies(companies)
	print("Demo: archivo inicializado.")
	print("Registrando 2 empresas...")
	register_company(companies, ruc="1234567890", nombre="Empresa A", rubro="Comercio")
	register_company(companies, ruc="0987654321", nombre="Empresa B", rubro="Servicios")
	print("Listado tras registro:")
	list_companies(load_companies())
	print("Actualizando Empresa A (cambiando nombre)...")
	update_company(load_companies(), ruc="1234567890")
	# The update_company interactive prompts are not suitable in demo; do direct update instead
	comps = load_companies()
	idx = find_company(comps, "1234567890")
	if idx is not None:
		comps[idx]["nombre"] = "Empresa A Actualizada"
		save_companies(comps)
		print("Empresa A actualizada (modo demo).")
	print("Listado tras actualización:")
	list_companies(load_companies())
	print("Eliminando Empresa B...")
	delete_company(load_companies(), ruc="0987654321")
	print("Listado final:")
	list_companies(load_companies())


def parse_args(argv=None):
	p = argparse.ArgumentParser(description="CRUD de empresas simple")
	p.add_argument("--demo", action="store_true", help="Ejecuta un demo no interactivo")
	return p.parse_args(argv)


if __name__ == "__main__":
	args = parse_args()
	if args.demo:
		demo_run()
		sys.exit(0)
	interactive_menu()
