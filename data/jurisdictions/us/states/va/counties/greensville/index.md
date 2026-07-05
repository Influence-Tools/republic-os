---
type: Jurisdiction
title: "Greensville County, VA"
classification: county
fips: "51081"
state: "VA"
demographics:
  population: 11275
  population_under_18: 1720
  population_18_64: 7717
  population_65_plus: 1838
  median_household_income: 54668
  poverty_rate: 14.25
  homeownership_rate: 66.33
  unemployment_rate: 6.31
  median_home_value: 159400
  gini_index: 0.4153
  vacancy_rate: 20.54
  race_white: 4015
  race_black: 6344
  race_asian: 26
  race_native: 18
  hispanic: 325
  bachelors_plus: 1541
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/va/districts/house/83"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Greensville County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11275 |
| Under 18 | 1720 |
| 18–64 | 7717 |
| 65+ | 1838 |
| Median household income | 54668 |
| Poverty rate | 14.25 |
| Homeownership rate | 66.33 |
| Unemployment rate | 6.31 |
| Median home value | 159400 |
| Gini index | 0.4153 |
| Vacancy rate | 20.54 |
| White | 4015 |
| Black | 6344 |
| Asian | 26 |
| Native | 18 |
| Hispanic/Latino | 325 |
| Bachelor's or higher | 1541 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 100% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
