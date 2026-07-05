---
type: Jurisdiction
title: "Effingham County, GA"
classification: county
fips: "13103"
state: "GA"
demographics:
  population: 69143
  population_under_18: 18257
  population_18_64: 42255
  population_65_plus: 8631
  median_household_income: 88438
  poverty_rate: 6.84
  homeownership_rate: 78.35
  unemployment_rate: 5.52
  median_home_value: 276000
  gini_index: 0.3943
  vacancy_rate: 6.38
  race_white: 51883
  race_black: 9995
  race_asian: 681
  race_native: 118
  hispanic: 4572
  bachelors_plus: 16138
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.5922
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.4049
  - to: "us/states/ga/districts/senate/4"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/159"
    rel: in-district
    area_weight: 0.779
  - to: "us/states/ga/districts/house/161"
    rel: in-district
    area_weight: 0.2202
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Effingham County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 69143 |
| Under 18 | 18257 |
| 18–64 | 42255 |
| 65+ | 8631 |
| Median household income | 88438 |
| Poverty rate | 6.84 |
| Homeownership rate | 78.35 |
| Unemployment rate | 5.52 |
| Median home value | 276000 |
| Gini index | 0.3943 |
| Vacancy rate | 6.38 |
| White | 51883 |
| Black | 9995 |
| Asian | 681 |
| Native | 118 |
| Hispanic/Latino | 4572 |
| Bachelor's or higher | 16138 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 59% (congressional)
- [GA-01](/us/states/ga/districts/01.md) — 40% (congressional)
- [GA Senate District 4](/us/states/ga/districts/senate/4.md) — 100% (state senate)
- [GA House District 159](/us/states/ga/districts/house/159.md) — 78% (state house)
- [GA House District 161](/us/states/ga/districts/house/161.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
