#!/usr/bin/env python3

import argparse
import secrets
import string

def generate_password(length, include_symbols: bool = False) -> str:
	lowercase = string.ascii_lowercase
	uppercase = string.ascii_uppercase
	digits = string.digits
	symbols = '!@#$%^&*()-+_=[]{};:|,./<>?'

	required_sets = [lowercase, uppercase, digits]
	if include_symbols:
		required_sets.append(symbols)

	pool = ''.join(required_sets)
	min_length = len(required_sets)

	if length < min_length:
		raise ValueError(f"Password length must be at least {min_length}")

	password_chars = [secrets.choice(charset) for charset in required_sets]
	remaining = length - len(password_chars)
	password_chars += [secrets.choice(pool) for _ in range(remaining)]

	# Securely shuffle the characters
	sr = secrets.SystemRandom()
	sr.shuffle(password_chars)

	return ''.join(password_chars)

def main():
	parser = argparse.ArgumentParser(description='Generate a secure password.')
	parser.add_argument('--length', type=int, default=12,
		help='Length of the password (default: 12)')
	parser.add_argument('--symbols', action='store_true',
		help='Include symbols in the password')

	args = parser.parse_args()

	try:
		password = generate_password(args.length, args.symbols)
		print(password)
	except ValueError as e:
		print(f"Error: {e}")
		exit(1)

if __name__ == '__main__':
	main()
