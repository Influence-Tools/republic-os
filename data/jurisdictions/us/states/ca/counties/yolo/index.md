---
type: Jurisdiction
title: "Yolo County, CA"
classification: county
fips: "06113"
state: "CA"
demographics:
  population: 220564
  population_under_18: 44283
  population_18_64: 146569
  population_65_plus: 29712
  median_household_income: 91752
  poverty_rate: 16.69
  homeownership_rate: 54.29
  unemployment_rate: 6.12
  median_home_value: 620700
  gini_index: 0.4834
  vacancy_rate: 6.98
  race_white: 107834
  race_black: 5795
  race_asian: 33861
  race_native: 2870
  hispanic: 73569
  bachelors_plus: 87220
districts:
  - to: "us/states/ca/districts/04"
    rel: in-district
    area_weight: 0.9591
  - to: "us/states/ca/districts/07"
    rel: in-district
    area_weight: 0.038
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ca/districts/house/4"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Yolo County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 220564 |
| Under 18 | 44283 |
| 18–64 | 146569 |
| 65+ | 29712 |
| Median household income | 91752 |
| Poverty rate | 16.69 |
| Homeownership rate | 54.29 |
| Unemployment rate | 6.12 |
| Median home value | 620700 |
| Gini index | 0.4834 |
| Vacancy rate | 6.98 |
| White | 107834 |
| Black | 5795 |
| Asian | 33861 |
| Native | 2870 |
| Hispanic/Latino | 73569 |
| Bachelor's or higher | 87220 |

## Districts

- [CA-04](/us/states/ca/districts/04.md) — 96% (congressional)
- [CA-07](/us/states/ca/districts/07.md) — 4% (congressional)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 100% (state senate)
- [CA House District 4](/us/states/ca/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
