# TASK 1 - ALGORITHM DESIGN REVIEW

## Diagnose and Repair Poor Pseudocode

### Problem Statement

A logistics company wants to load packages into a delivery vehicle.

Each package has:

- A weight
- A value

Packages may be divided if necessary.

The objective is to maximise the total value loaded without exceeding the vehicle capacity.

The given junior engineer pseudocode is:

```text
ALGORITHM LoadVehicle

BEGIN
    Read packages
    Arrange packages
    Select the best package

    WHILE vehicle has space DO
        Add suitable package
    END WHILE

    Calculate value
    RETURN result
END
