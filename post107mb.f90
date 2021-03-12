
PROGRAM CODE_1

  IMPLICIT NONE

  INTEGER :: FLO_NUM = 1
  INTEGER :: MY_IOSTAT
  CHARACTER (256) :: MY_IOMSG
  INTEGER :: N
  INTEGER :: ID
  INTEGER :: I, J, K, P
  INTEGER :: S, ARRAY_COUNTER, IPOS_4, LOW_LIM, HIGH_LIM, STORE_POINTS, K_COUNTER
  INTEGER :: IPOS, IPOS_2, IPOS_3, COUNTER, STOP_COUNTER, LENGTH, LINE_COUNTER
  REAL, DIMENSION(:), ALLOCATABLE:: STORE_J
  INTEGER, PARAMETER :: NLEN = 100
  CHARACTER (LEN=NLEN) :: STR, FORMAT_A, NUM_2, BRACKET, STR_REST
  CHARACTER (1000) :: STR_FLO
  CHARACTER (1000) :: REPLACE_DIM
  REAL :: NUM, BLOCK_ID
  REAL, DIMENSION (:), ALLOCATABLE:: ARRAY_BLOCK_SUB
  REAL, DIMENSION (:), ALLOCATABLE:: ARRAY_I_J_SUB
  REAL, DIMENSION (:), ALLOCATABLE:: ARRAY_BLOCK
  REAL, DIMENSION (:), ALLOCATABLE:: ARRAY_I_J
  REAL, DIMENSION (:), ALLOCATABLE:: ARRAY_ID

  !Following VARIABLES for output
  INTEGER :: WING_LINES
  INTEGER :: TOTAL_LINES
  INTEGER :: WING_POINTS
  CHARACTER (1000) :: STR_WING
  CHARACTER (1000) :: NAME_1, INTEGER_1, NAME_2
  CHARACTER (1000) :: QUOTATION
  INTEGER :: I_SUM, J_SUM, K_SUM
  INTEGER :: BIGGEST_NUM, IDEX


  !ADDING CP EXTRACTION VARIABLES
  INTEGER :: CHECKED_INT
  CHARACTER (1000) :: FINAL_VAR, EXTRACT_1, EXTRACT_2, EXTRACT_3, EXTRACT_4
  INTEGER :: IPOS_15
  INTEGER :: START_IND, END_IND

  !EXTRACT THE BIGGEST ITERATION NUMBER FROM THE LIST
  DO I = 0, 100

    IF (I.LT.10) THEN
        WRITE(INTEGER_1, "(I1)") I
        NAME_1 = TRIM(('flo.case'//'1'//'.0'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
    ELSE
        WRITE(INTEGER_1, *) I
        NAME_1 = TRIM(('flo.case'//'1'//'.'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
    END IF

    OPEN(FLO_NUM+1, FILE=NAME_1, STATUS = 'OLD', IOSTAT=MY_IOSTAT, IOMSG=MY_IOMSG)

    IF(MY_IOSTAT /= 0) THEN
        !PRINT*, TRIM(NAME_1)
        !PRINT*, TRIM(INTEGER_1)
        !PRINT*, I
      CONTINUE
    ELSE
        !PRINT*, "I OPENED ", I
        BIGGEST_NUM = I
        !PRINT*, "FOUND IT ", BIGGEST_NUM
        CLOSE(FLO_NUM+1)
    END IF

  END DO


  DO IDEX = 1, 2

    IF (IDEX.EQ.1) THEN
      NAME_1 = "flo.case1.00.dat"
      NAME_2 = "Wing_Analysis_1.00.dat"
    ELSE
      !CHECK WHETHER IT IS SMALLER OR GREATER THAN 10
      IF (BIGGEST_NUM.LT.10) THEN
          WRITE(INTEGER_1, "(I1)") BIGGEST_NUM
          NAME_1 = TRIM(('flo.case'//'1'//'.0'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
          NAME_2 = TRIM(('Wing_Analysis_1.0'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
      ELSE
          WRITE(INTEGER_1, *) BIGGEST_NUM
          NAME_1 = TRIM(('flo.case'//'1'//'.'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
          NAME_2 = TRIM(('Wing_Analysis_1.'//TRIM(ADJUSTL(INTEGER_1))))//".dat"
      END IF
    END IF

    !OPEN THE FLO.CASE.1.##.DAT
    OPEN(FLO_NUM+1, FILE = TRIM(NAME_1))

    !OPEN NEW WING_ANALYSIS FILE
    OPEN(FLO_NUM, FILE = TRIM(NAME_2), STATUS = 'NEW', IOSTAT=MY_IOSTAT, IOMSG=MY_IOMSG)

    IF(MY_IOSTAT /= 0) THEN
      OPEN(FLO_NUM, FILE = TRIM(NAME_2), STATUS = 'OLD', IOSTAT=MY_IOSTAT, IOMSG=MY_IOMSG)
    END IF


    !THIS IS THE CODE THAT EXTRACTS THE RHO0, U0, V0
    CHECKED_INT = 0
    OPEN(15, FILE="output", STATUS = 'OLD', IOSTAT=MY_IOSTAT, IOMSG=MY_IOMSG)

    DO WHILE(CHECKED_INT.NE.1)

        READ(15, FMT=16) FINAL_VAR
        IPOS_15 = INDEX(FINAL_VAR, "FINAL INLET VARIABLES")

        !IF WE FIND THE ZONE STARTING LINE
        IF (IPOS_15.NE.0) THEN
            !PRINT*, TRIM(FINAL_VAR)
            READ(15, FMT=16) FINAL_VAR
            READ(15, FMT=16) FINAL_VAR
            !PRINT*, TRIM(FINAL_VAR)

            START_IND = 3
            END_IND = 13
            READ(FINAL_VAR(START_IND:END_IND), *) EXTRACT_1
            !PRINT*, TRIM(EXTRACT_1) !THIS IS THE RHO0

            START_IND = 15
            END_IND = 25
            READ(FINAL_VAR(START_IND:END_IND), *) EXTRACT_2
            !PRINT*, TRIM(EXTRACT_2) !THIS IS THE P0

            START_IND = 39
            END_IND = 49
            READ(FINAL_VAR(START_IND:END_IND), *) EXTRACT_3
            !PRINT*, TRIM(EXTRACT_2) !THIS IS THE U0

            START_IND = 51
            END_IND = 61
            READ(FINAL_VAR(START_IND:END_IND), *) EXTRACT_4
            !PRINT*, TRIM(EXTRACT_3) !THSI IS THE V0

            CHECKED_INT = CHECKED_INT + 1

        END IF

    END DO

    CLOSE(15)

    !THIS BEGINGS THE LOOPING INSIDE MBL1.CONN
    OPEN(FLO_NUM+2, FILE="MBL1.CONN")
    READ(FLO_NUM+2, FMT=15) ID

    PRINT*,""
    PRINT*,""

    IF (IDEX.EQ.1) THEN
      PRINT*, "***************************************************************************"
      PRINT*, "*                                                                         *"
      PRINT*, "*                         START OF POSTPROCESSING                         *"
      PRINT*, "*                                                                         *"
      PRINT*, "***************************************************************************"

      PRINT*, ""
      PRINT*, "                             STATUS - RUNNING                              "
      PRINT*, ""
    END IF

    PRINT*, ""
    PRINT*, "********************** TEST CASE - DESIGN ITERATION - ", TRIM(NAME_1), " **********************"

    PRINT *, ""
    PRINT *, "**********************************"
    PRINT *, "TOTAL BLOCK COUNT = ", ID
    PRINT *, "**********************************"
    CLOSE(FLO_NUM+2)
    N = ID

    ALLOCATE (ARRAY_BLOCK_SUB(N))
    ALLOCATE (ARRAY_I_J_SUB(N))

    OPEN(FLO_NUM+3, FILE="MBL1.CONN")
    ! OPEN(UNIT=3, FILE = 'Analysis.dat', STATUS = 'NEW')

    COUNTER = 0

    !START LOOKING FOR THE "-7" IN THE MBL1.CONN
    DO S = 1, N+1
        READ(FLO_NUM+3, FMT=16, IOSTAT=MY_IOSTAT, IOMSG=MY_IOMSG) STR
        IPOS = SCAN(STR,"-",BACK=.FALSE.)
        READ (STR(1+IPOS:),*) NUM

        DO WHILE (NUM.NE.7)
          STR_REST = TRIM(STR(1+IPOS:))
          IPOS_2 = SCAN(STR_REST,"-",BACK=.FALSE.)
          IPOS = SCAN(STR_REST,"-",BACK=.FALSE.) + IPOS
          READ(STR_REST(1+IPOS_2:),*) NUM
          IF (IPOS_2.EQ.0) THEN
              EXIT
          END IF
        END DO

        IF (IPOS.NE.0.AND.NUM.EQ.7) THEN

          READ(STR(1:), *) BLOCK_ID

          ARRAY_BLOCK_SUB(COUNTER+1) = BLOCK_ID
          ARRAY_I_J_SUB(COUNTER+1) = IPOS

          !IPOS = 36 - J
          !IPOS = 6 - I

          COUNTER = COUNTER + 1

        END IF

    END DO

    ALLOCATE (ARRAY_BLOCK(COUNTER))
    ALLOCATE (ARRAY_I_J(COUNTER))

    ARRAY_BLOCK = ARRAY_BLOCK_SUB(1:COUNTER)
    ARRAY_I_J = ARRAY_I_J_SUB(1:COUNTER)

    PRINT*,""
    PRINT*, "BLOCK NUMBER CORRESPONDING TO WING"
    PRINT*, ""
    WRITE(*,'(6F10.1)') ARRAY_BLOCK
    PRINT*,""

    PRINT*, "POSITION INDEX OF -7 ON EACH LINE IN MBL1.CONN"
    PRINT*, ""
    WRITE(*,'(6F10.1)') ARRAY_I_J
    PRINT*,""
    DEALLOCATE (ARRAY_BLOCK_SUB)
    DEALLOCATE (ARRAY_I_J_SUB)
    PRINT*, "NUMBER OF BLOCKS TO WING =", COUNTER

    PRINT*,""
    ALLOCATE (ARRAY_ID(COUNTER))
    ARRAY_ID = (/(I, I=1, COUNTER)/)
    WRITE(*,'(6F10.1)') ARRAY_ID
    PRINT*, ""

    STOP_COUNTER = 1
    LINE_COUNTER = 1
    ARRAY_COUNTER = 1
    I_SUM = 0
    J_SUM = 0
    K_SUM = 0

    DO WHILE(ARRAY_COUNTER.LE.COUNTER)
      READ(FLO_NUM+1, FMT=17) STR_FLO
      !PRINT*, TRIM(STR_FLO)
      !IPOS_3 = INDEX(STR_FLO,"F=POINT",BACK=.FALSE.)

      !WRITES THE TOP TWO LINES FOR STORING TITLE AND VARIABLES
      IF (LINE_COUNTER.LE.2) THEN

        IF (LINE_COUNTER.EQ.1) THEN
          WRITE(FLO_NUM, *) STR_FLO
        END IF

        !THIS WILL ADD CP TO THE LIST OF VARIABLES
        IF (LINE_COUNTER.EQ.2) THEN

          QUOTATION = "FILETYPE = FULL"
          IF (STR_FLO(2:17).EQ.QUOTATION) THEN
            READ(FLO_NUM+1, FMT=17) STR_FLO
          END IF

          QUOTATION = TRIM(STR_FLO)//' "RHO0" "P0" "U0" "V0" '
          WRITE(FLO_NUM, *) QUOTATION
        END IF
      END IF

      IPOS_3 = INDEX(STR_FLO, "F=POINT")

      !IF WE FIND THE ZONE STARTING LINE
      IF (IPOS_3.NE.0) THEN

        !STOP_COUNTER = WHICH BLOCK WE ARE AT
        IF (STOP_COUNTER.EQ.ARRAY_BLOCK(ARRAY_COUNTER)) THEN

          PRINT*,""
          PRINT*, "BLOCK NUMBER = ", STOP_COUNTER
          PRINT*, "START DATA FOR ZONE AT LINE ", LINE_COUNTER - 1

          WRITE(FLO_NUM, *) "ZONE"

          !EXTRACT I TEXT
          IPOS_4 = INDEX(STR_FLO, "I =", BACK=.FALSE.)
          LOW_LIM = IPOS_4 + 3
          HIGH_LIM = IPOS_4 + 5
          READ(STR_FLO(LOW_LIM:HIGH_LIM), *) I
          !WRITE(FLO_NUM, "(I2)") I

          ! IN CASE WE HAVE LIMIT ON I DUE TO -7 IN I-COLUMN IN MBL1.CONN
          IF (ARRAY_I_J(ARRAY_COUNTER).EQ.6) THEN
            !WRITE NEW LINE WITH I = 0 OR J = 0
            REPLACE_DIM = STR_FLO(1:LOW_LIM)
            REPLACE_DIM = TRIM(REPLACE_DIM)//" 1"
            REPLACE_DIM = TRIM(REPLACE_DIM)//STR_FLO((HIGH_LIM+1):)
            WRITE(FLO_NUM, *) TRIM(REPLACE_DIM)
          END IF

          !EXTRACT J TEXT
          IPOS_4 = INDEX(STR_FLO, "J =", BACK=.FALSE.)
          LOW_LIM = IPOS_4 + 3
          HIGH_LIM = IPOS_4 + 5
          READ(STR_FLO(LOW_LIM:HIGH_LIM), *) J
          !WRITE(FLO_NUM, "(I2)") J

          !IN CASE WE HAVE LIMIT ON J DUE TO -7 IN J-COLUMN IN MBL1.CONN
          IF (ARRAY_I_J(ARRAY_COUNTER).EQ.36) THEN
            !WRITE NEW LINE WITH I = 0 OR J = 0
            REPLACE_DIM = STR_FLO(1:LOW_LIM)
            REPLACE_DIM = TRIM(REPLACE_DIM)//" 1"
            REPLACE_DIM = TRIM(REPLACE_DIM)//STR_FLO((HIGH_LIM+1):)
            WRITE(FLO_NUM, *) TRIM(REPLACE_DIM)
          END IF

          !EXTRACT K TEXT
          IPOS_4 = INDEX(STR_FLO, "K =", BACK=.FALSE.)
          LOW_LIM = IPOS_4 + 3
          HIGH_LIM = IPOS_4 + 5
          READ(STR_FLO(LOW_LIM:HIGH_LIM), *) K
          !WRITE(FLO_NUM, "(I2)") K

          !CALCULATE POINTS FOR WING AND TOTAL FOR BLOCK
          WING_LINES = I*J
          TOTAL_LINES = I*J*K

          STORE_POINTS = 1
          ALLOCATE (STORE_J(K))

          IF (ARRAY_I_J(ARRAY_COUNTER).EQ.36) THEN
            !BUILDS UP THE LINE OF CODE TO WHERE WE SHOULD START WRITING
            !THE LINE OF CODES FOR -7 IN THE J-COLUMN IN MBL1.CONN
            DO WHILE(STORE_POINTS.LE.K)

              IF (STORE_POINTS.EQ.1) THEN
                STORE_J(STORE_POINTS) = 1
              END IF

              IF (STORE_POINTS.GE.2) THEN
                IF (STORE_POINTS.EQ.2) THEN
                  STORE_J(STORE_POINTS) = WING_LINES
                ELSE
                  STORE_J(STORE_POINTS) = STORE_J(STORE_POINTS-1) + WING_LINES
                END IF
              END IF

              STORE_POINTS = STORE_POINTS + 1
            END DO
          END IF

          PRINT*, "WING DATA POINTS =", WING_LINES
          PRINT*, "TOTAL DATA POINTS =", TOTAL_LINES
          PRINT*, "I_TOTAL = ", I
          PRINT*, "J_TOTAL = ", J
          PRINT*, "K_TOTAL = ", K
          !PRINT*, "STARTING LINE FOR WING POINTS ="
          !PRINT*, ""
          !WRITE(*,'(5F10.1)') STORE_J
          !PRINT*, ""

          WING_POINTS = 1
          STORE_POINTS = 1
          K_COUNTER = 1

          !******************************** START OF WRITING FILES **************************************


!0.0000000E+00     0.7500000E+00     0.2500000E+00
            !WRITE THE POINTS IN THE FILE
            DO WHILE (WING_POINTS.LE.TOTAL_LINES)

              IF (ARRAY_I_J(ARRAY_COUNTER).EQ.6) THEN

                !USE K_COUNTER HERE TO COUNT WHICH LINE WE ARE GOING TO WRITE THE DATA

                READ(FLO_NUM+1, FMT=17) STR_WING

                IF (WING_POINTS.EQ.K_COUNTER)THEN

                  QUOTATION = TRIM(STR_WING)//"     "//EXTRACT_1
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_2
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_3
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_4
                  QUOTATION = TRIM(QUOTATION)//"E+00"

                  WRITE(FLO_NUM, *) QUOTATION
                  !PRINT*, STORE_POINTS
                  !STORE_POINTS = STORE_POINTS + 1
                  K_COUNTER = K_COUNTER + I
                  I_SUM = I_SUM + 1

                END IF

                ! !RECOUNT THE I OR J
                ! IF (STORE_POINTS.EQ.J) THEN
                !   STORE_POINTS = 1
                !   !PRINT*, "K = ", K_COUNTER
                !   !PRINT*, "I STARTING LINE = ", STORE_J(K_COUNTER)
                ! END IF

                WING_POINTS = WING_POINTS + 1
                !KEEP TRACK OF WHERE WE ARE IN THE FILE
                LINE_COUNTER = LINE_COUNTER + 1

              END IF

              IF (ARRAY_I_J(ARRAY_COUNTER).EQ.36) THEN
                READ(FLO_NUM+1, FMT=17) STR_WING

                IF (STORE_POINTS.LE.I)THEN
                  QUOTATION = TRIM(STR_WING)//"     "//EXTRACT_1
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_2
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_3
                  QUOTATION = TRIM(QUOTATION)//"E+00"
                  QUOTATION = TRIM(QUOTATION)//"     "//EXTRACT_4
                  QUOTATION = TRIM(QUOTATION)//"E+00"

                  WRITE(FLO_NUM, *) QUOTATION
                  !PRINT*, STORE_POINTS
                  STORE_POINTS = STORE_POINTS + 1
                  I_SUM = I_SUM + 1
                END IF

                !RECOUNT THE I OR J
                IF (WING_POINTS.EQ.STORE_J(K_COUNTER+1)) THEN
                  STORE_POINTS = 1
                  !PRINT*, "K = ", K_COUNTER
                  !PRINT*, "I STARTING LINE = ", STORE_J(K_COUNTER)
                  K_COUNTER = K_COUNTER + 1
                END IF

                WING_POINTS = WING_POINTS + 1
                !KEEP TRACK OF WHERE WE ARE IN THE FILE
                LINE_COUNTER = LINE_COUNTER + 1

              END IF

            END DO

          !PRINT THE FINAL LINE OF CODE FOR THE BLOCK
          PRINT*, "FINAL DATA FOR ZONE AT LINE", LINE_COUNTER
          PRINT*, ""
          !THIS UPDATES HOW MANY TIMES WE WROTE THE ZONES FOR THE WING
          ARRAY_COUNTER = ARRAY_COUNTER + 1
          DEALLOCATE (STORE_J)
          END IF

          !THIS UPDATES WHICH ZONE WE ARE AT
          STOP_COUNTER = STOP_COUNTER + 1
        END IF

      !LENGTH = LEN_TRIM(STR_FLO)
      !PRINT*,LENGTH
      !PRINT*,TRIM(STR_FLO)
      !WRITE(FLO_NUM, *) TRIM(STR_FLO)

      LINE_COUNTER = LINE_COUNTER + 1

    END DO

    PRINT*, ""
    PRINT*, "***************************************"
    PRINT*, "TOTAL WING DATA POINTS = ", I_SUM
    PRINT*, "***************************************"
    !PRINT*, "TOTAL J = ", J_SUM
    !PRINT*, "TOTAL K = ", K_SUM

    CLOSE(FLO_NUM)
    CLOSE(FLO_NUM+3)
    DEALLOCATE(ARRAY_BLOCK)
    DEALLOCATE(ARRAY_I_J)
    DEALLOCATE(ARRAY_ID)

  END DO

    PRINT*, ""
    PRINT*, ""
    PRINT*, "***************************************************************************"
    PRINT*, "*                                                                         *"
    PRINT*, "*                          END OF POSTPROCESSING                          *"
    PRINT*, "*                                                                         *"
    PRINT*, "***************************************************************************"

  !FORMATTING
  15 FORMAT(I100)
  16 FORMAT(A1000)
  17 FORMAT(A1000)
  4 FORMAT(I3)

END PROGRAM CODE_1

