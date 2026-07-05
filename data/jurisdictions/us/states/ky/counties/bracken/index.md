---
type: Jurisdiction
title: "Bracken County, KY"
classification: county
fips: "21023"
state: "KY"
demographics:
  population: 8444
  population_under_18: 1950
  population_18_64: 4961
  population_65_plus: 1533
  median_household_income: 66319
  poverty_rate: 19.52
  homeownership_rate: 78.54
  unemployment_rate: 4.76
  median_home_value: 125000
  gini_index: 0.4421
  vacancy_rate: 12.85
  race_white: 8080
  race_black: 54
  race_asian: 7
  race_native: 84
  hispanic: 125
  bachelors_plus: 1588
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/senate/24"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/house/70"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Bracken County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8444 |
| Under 18 | 1950 |
| 18–64 | 4961 |
| 65+ | 1533 |
| Median household income | 66319 |
| Poverty rate | 19.52 |
| Homeownership rate | 78.54 |
| Unemployment rate | 4.76 |
| Median home value | 125000 |
| Gini index | 0.4421 |
| Vacancy rate | 12.85 |
| White | 8080 |
| Black | 54 |
| Asian | 7 |
| Native | 84 |
| Hispanic/Latino | 125 |
| Bachelor's or higher | 1588 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 24](/us/states/ky/districts/senate/24.md) — 100% (state senate)
- [KY House District 70](/us/states/ky/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
