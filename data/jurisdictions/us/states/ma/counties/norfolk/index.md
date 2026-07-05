---
type: Jurisdiction
title: "Norfolk County, MA"
classification: county
fips: "25021"
state: "MA"
demographics:
  population: 730082
  population_under_18: 149313
  population_18_64: 451124
  population_65_plus: 129645
  median_household_income: 130739
  poverty_rate: 6.69
  homeownership_rate: 68.75
  unemployment_rate: 4.94
  median_home_value: 683900
  gini_index: 0.4841
  vacancy_rate: 4.02
  race_white: 509654
  race_black: 54240
  race_asian: 90735
  race_native: 706
  hispanic: 42383
  bachelors_plus: 451470
districts:
  - to: "us/states/ma/districts/04"
    rel: in-district
    area_weight: 0.463
  - to: "us/states/ma/districts/08"
    rel: in-district
    area_weight: 0.3729
  - to: "us/states/ma/districts/07"
    rel: in-district
    area_weight: 0.0393
  - to: "us/states/ma/districts/02"
    rel: in-district
    area_weight: 0.026
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.0234
  - to: "us/states/ma/districts/05"
    rel: in-district
    area_weight: 0.0169
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Norfolk County, MA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 730082 |
| Under 18 | 149313 |
| 18–64 | 451124 |
| 65+ | 129645 |
| Median household income | 130739 |
| Poverty rate | 6.69 |
| Homeownership rate | 68.75 |
| Unemployment rate | 4.94 |
| Median home value | 683900 |
| Gini index | 0.4841 |
| Vacancy rate | 4.02 |
| White | 509654 |
| Black | 54240 |
| Asian | 90735 |
| Native | 706 |
| Hispanic/Latino | 42383 |
| Bachelor's or higher | 451470 |

## Districts

- [MA-04](/us/states/ma/districts/04.md) — 46% (congressional)
- [MA-08](/us/states/ma/districts/08.md) — 37% (congressional)
- [MA-07](/us/states/ma/districts/07.md) — 4% (congressional)
- [MA-02](/us/states/ma/districts/02.md) — 3% (congressional)
- [MA-09](/us/states/ma/districts/09.md) — 2% (congressional)
- [MA-05](/us/states/ma/districts/05.md) — 2% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
