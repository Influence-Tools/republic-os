---
type: Jurisdiction
title: "Wapello County, IA"
classification: county
fips: "19179"
state: "IA"
demographics:
  population: 35362
  population_under_18: 8432
  population_18_64: 20434
  population_65_plus: 6496
  median_household_income: 64766
  poverty_rate: 15.84
  homeownership_rate: 68.41
  unemployment_rate: 4.29
  median_home_value: 125100
  gini_index: 0.4426
  vacancy_rate: 11.02
  race_white: 27965
  race_black: 1068
  race_asian: 634
  race_native: 155
  hispanic: 4748
  bachelors_plus: 6540
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/25"
    rel: in-district
    area_weight: 0.579
  - to: "us/states/ia/districts/house/26"
    rel: in-district
    area_weight: 0.4209
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Wapello County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35362 |
| Under 18 | 8432 |
| 18–64 | 20434 |
| 65+ | 6496 |
| Median household income | 64766 |
| Poverty rate | 15.84 |
| Homeownership rate | 68.41 |
| Unemployment rate | 4.29 |
| Median home value | 125100 |
| Gini index | 0.4426 |
| Vacancy rate | 11.02 |
| White | 27965 |
| Black | 1068 |
| Asian | 634 |
| Native | 155 |
| Hispanic/Latino | 4748 |
| Bachelor's or higher | 6540 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 13](/us/states/ia/districts/senate/13.md) — 100% (state senate)
- [IA House District 25](/us/states/ia/districts/house/25.md) — 58% (state house)
- [IA House District 26](/us/states/ia/districts/house/26.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
