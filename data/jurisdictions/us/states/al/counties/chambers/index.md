---
type: Jurisdiction
title: "Chambers County, AL"
classification: county
fips: "01017"
state: "AL"
demographics:
  population: 34192
  population_under_18: 7149
  population_18_64: 20104
  population_65_plus: 6939
  median_household_income: 49656
  poverty_rate: 15.74
  homeownership_rate: 71.78
  unemployment_rate: 5.14
  median_home_value: 135800
  gini_index: 0.4403
  vacancy_rate: 18.26
  race_white: 18794
  race_black: 13131
  race_asian: 81
  race_native: 51
  hispanic: 1372
  bachelors_plus: 4819
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/al/districts/senate/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/37"
    rel: in-district
    area_weight: 0.7733
  - to: "us/states/al/districts/house/38"
    rel: in-district
    area_weight: 0.2264
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Chambers County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34192 |
| Under 18 | 7149 |
| 18–64 | 20104 |
| 65+ | 6939 |
| Median household income | 49656 |
| Poverty rate | 15.74 |
| Homeownership rate | 71.78 |
| Unemployment rate | 5.14 |
| Median home value | 135800 |
| Gini index | 0.4403 |
| Vacancy rate | 18.26 |
| White | 18794 |
| Black | 13131 |
| Asian | 81 |
| Native | 51 |
| Hispanic/Latino | 1372 |
| Bachelor's or higher | 4819 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 13](/us/states/al/districts/senate/13.md) — 100% (state senate)
- [AL House District 37](/us/states/al/districts/house/37.md) — 77% (state house)
- [AL House District 38](/us/states/al/districts/house/38.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
