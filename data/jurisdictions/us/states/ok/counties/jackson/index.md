---
type: Jurisdiction
title: "Jackson County, OK"
classification: county
fips: "40065"
state: "OK"
demographics:
  population: 24678
  population_under_18: 6150
  population_18_64: 14674
  population_65_plus: 3854
  median_household_income: 62799
  poverty_rate: 16.16
  homeownership_rate: 59.21
  unemployment_rate: 5.59
  median_home_value: 158400
  gini_index: 0.4334
  vacancy_rate: 19.03
  race_white: 17698
  race_black: 1587
  race_asian: 416
  race_native: 388
  hispanic: 6162
  bachelors_plus: 5458
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9946
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ok/districts/house/52"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Jackson County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24678 |
| Under 18 | 6150 |
| 18–64 | 14674 |
| 65+ | 3854 |
| Median household income | 62799 |
| Poverty rate | 16.16 |
| Homeownership rate | 59.21 |
| Unemployment rate | 5.59 |
| Median home value | 158400 |
| Gini index | 0.4334 |
| Vacancy rate | 19.03 |
| White | 17698 |
| Black | 1587 |
| Asian | 416 |
| Native | 388 |
| Hispanic/Latino | 6162 |
| Bachelor's or higher | 5458 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 99% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 52](/us/states/ok/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
