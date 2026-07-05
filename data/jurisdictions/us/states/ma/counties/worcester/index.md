---
type: Jurisdiction
title: "Worcester County, MA"
classification: county
fips: "25027"
state: "MA"
demographics:
  population: 867788
  population_under_18: 178921
  population_18_64: 541177
  population_65_plus: 147690
  median_household_income: 95939
  poverty_rate: 10.33
  homeownership_rate: 65.78
  unemployment_rate: 5.27
  median_home_value: 423700
  gini_index: 0.4525
  vacancy_rate: 5.45
  race_white: 630934
  race_black: 45228
  race_asian: 46238
  race_native: 2170
  hispanic: 118968
  bachelors_plus: 343880
districts:
  - to: "us/states/ma/districts/02"
    rel: in-district
    area_weight: 0.587
  - to: "us/states/ma/districts/01"
    rel: in-district
    area_weight: 0.1949
  - to: "us/states/ma/districts/03"
    rel: in-district
    area_weight: 0.1838
  - to: "us/states/ma/districts/04"
    rel: in-district
    area_weight: 0.0342
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Worcester County, MA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 867788 |
| Under 18 | 178921 |
| 18–64 | 541177 |
| 65+ | 147690 |
| Median household income | 95939 |
| Poverty rate | 10.33 |
| Homeownership rate | 65.78 |
| Unemployment rate | 5.27 |
| Median home value | 423700 |
| Gini index | 0.4525 |
| Vacancy rate | 5.45 |
| White | 630934 |
| Black | 45228 |
| Asian | 46238 |
| Native | 2170 |
| Hispanic/Latino | 118968 |
| Bachelor's or higher | 343880 |

## Districts

- [MA-02](/us/states/ma/districts/02.md) — 59% (congressional)
- [MA-01](/us/states/ma/districts/01.md) — 19% (congressional)
- [MA-03](/us/states/ma/districts/03.md) — 18% (congressional)
- [MA-04](/us/states/ma/districts/04.md) — 3% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
