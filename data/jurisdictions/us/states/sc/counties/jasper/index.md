---
type: Jurisdiction
title: "Jasper County, SC"
classification: county
fips: "45053"
state: "SC"
demographics:
  population: 32166
  population_under_18: 5883
  population_18_64: 18856
  population_65_plus: 7427
  median_household_income: 65613
  poverty_rate: 17.83
  homeownership_rate: 77.16
  unemployment_rate: 4.57
  median_home_value: 325500
  gini_index: 0.4413
  vacancy_rate: 11.11
  race_white: 15468
  race_black: 10572
  race_asian: 286
  race_native: 334
  hispanic: 5661
  bachelors_plus: 8000
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.9248
  - to: "us/states/sc/districts/01"
    rel: in-district
    area_weight: 0.0299
  - to: "us/states/sc/districts/senate/45"
    rel: in-district
    area_weight: 0.9291
  - to: "us/states/sc/districts/senate/46"
    rel: in-district
    area_weight: 0.0269
  - to: "us/states/sc/districts/house/122"
    rel: in-district
    area_weight: 0.7662
  - to: "us/states/sc/districts/house/123"
    rel: in-district
    area_weight: 0.1629
  - to: "us/states/sc/districts/house/120"
    rel: in-district
    area_weight: 0.0268
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Jasper County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32166 |
| Under 18 | 5883 |
| 18–64 | 18856 |
| 65+ | 7427 |
| Median household income | 65613 |
| Poverty rate | 17.83 |
| Homeownership rate | 77.16 |
| Unemployment rate | 4.57 |
| Median home value | 325500 |
| Gini index | 0.4413 |
| Vacancy rate | 11.11 |
| White | 15468 |
| Black | 10572 |
| Asian | 286 |
| Native | 334 |
| Hispanic/Latino | 5661 |
| Bachelor's or higher | 8000 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 92% (congressional)
- [SC-01](/us/states/sc/districts/01.md) — 3% (congressional)
- [SC Senate District 45](/us/states/sc/districts/senate/45.md) — 93% (state senate)
- [SC Senate District 46](/us/states/sc/districts/senate/46.md) — 3% (state senate)
- [SC House District 122](/us/states/sc/districts/house/122.md) — 77% (state house)
- [SC House District 123](/us/states/sc/districts/house/123.md) — 16% (state house)
- [SC House District 120](/us/states/sc/districts/house/120.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
