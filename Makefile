.PONY: all check clean

GFOR = gfortran


all: check

check:
	@echo ""
	@${GFOR} post107mb.f90
	@./a.out

clean:
	@echo "Cleaning up *.out files..."
	@rm a.out
	@echo "Done..."
