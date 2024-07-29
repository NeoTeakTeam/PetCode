PY        := python3
BUILD_LIB := nuitka
LIBFLAGS  := 

TARGET    := Windows
VERSION   := debug

SRC       := ../../src
OUTPUT    := $(TARGET)/$(VERSION)


build: $(SRC)/main.py
	@echo "[ 01 ] PY     $(SRC)/main.py"
	@python -m nuitka --lto=no --onefile --standalone --output-dir="$(OUTPUT)" $(LIBFLAGS) "$(SRC)/main.py"


ifeq ($(VERSION),release)
ifeq ($(TARGET),Windows)
	@echo "[ 02 ] MV $(OUTPUT)/main.exe"
	@mv $(OUTPUT)/main.exe $(OUTPUT)/petcode.exe
else
ifeq ($(TARGET),Linux)
	@echo "[ 02 ] MV $(OUTPUT)/main.bin"
	@mv $(OUTPUT)/main.bin $(OUTPUT)/petcode
else
	@echo "Error! Unsupported system"
	@exit 2
endif
endif
	@echo
	@echo "Env Set!"
	@echo "PetCodeAssetsPath = (PetCode Assets Folder Path)"
else
	@echo
	@echo "Warn! Used Debug mode"
endif


install:
	@mkdir $(OUTPUT)
ifeq ($(VERSION),release)
ifeq ($(TARGET),Linux)
	@echo "[ 01 ] MV $(OUTPUT)/petcode"
	@echo "[ 01 ] Need Root"
	@su root -c "mv $(OUTPUT)/petcode /bin/petcode"

	@echo
	@echo "Env Set!"
	@echo "PetCodeAssetsPath = (PetCode Assets Folder Path)"

else
ifeq ($(TARGET),Windows)
	@echo
	@echo "Env Set!"
	@echo "PetCodeAssetsPath = (PetCode Assets Folder Path)"
	@echo "Path += $(OUTPUT)/petcode.exe"

else
	@echo "Error! Unsupported system"
	@exit 2
endif

endif
else
	@echo
	@echo "Warn! Used Debug mode"

endif
