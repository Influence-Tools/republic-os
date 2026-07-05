---
type: Jurisdiction
title: "Hendricks County, IN"
classification: county
fips: "18063"
state: "IN"
demographics:
  population: 183344
  population_under_18: 44976
  population_18_64: 110782
  population_65_plus: 27586
  median_household_income: 101144
  poverty_rate: 5.33
  homeownership_rate: 78.23
  unemployment_rate: 2.56
  median_home_value: 307600
  gini_index: 0.3924
  vacancy_rate: 3.68
  race_white: 143308
  race_black: 18514
  race_asian: 6078
  race_native: 518
  hispanic: 9546
  bachelors_plus: 66079
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/24"
    rel: in-district
    area_weight: 0.4903
  - to: "us/states/in/districts/senate/7"
    rel: in-district
    area_weight: 0.3011
  - to: "us/states/in/districts/senate/35"
    rel: in-district
    area_weight: 0.2085
  - to: "us/states/in/districts/house/28"
    rel: in-district
    area_weight: 0.7398
  - to: "us/states/in/districts/house/40"
    rel: in-district
    area_weight: 0.1061
  - to: "us/states/in/districts/house/25"
    rel: in-district
    area_weight: 0.0849
  - to: "us/states/in/districts/house/57"
    rel: in-district
    area_weight: 0.069
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Hendricks County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 183344 |
| Under 18 | 44976 |
| 18–64 | 110782 |
| 65+ | 27586 |
| Median household income | 101144 |
| Poverty rate | 5.33 |
| Homeownership rate | 78.23 |
| Unemployment rate | 2.56 |
| Median home value | 307600 |
| Gini index | 0.3924 |
| Vacancy rate | 3.68 |
| White | 143308 |
| Black | 18514 |
| Asian | 6078 |
| Native | 518 |
| Hispanic/Latino | 9546 |
| Bachelor's or higher | 66079 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 24](/us/states/in/districts/senate/24.md) — 49% (state senate)
- [IN Senate District 7](/us/states/in/districts/senate/7.md) — 30% (state senate)
- [IN Senate District 35](/us/states/in/districts/senate/35.md) — 21% (state senate)
- [IN House District 28](/us/states/in/districts/house/28.md) — 74% (state house)
- [IN House District 40](/us/states/in/districts/house/40.md) — 11% (state house)
- [IN House District 25](/us/states/in/districts/house/25.md) — 8% (state house)
- [IN House District 57](/us/states/in/districts/house/57.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
