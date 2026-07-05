---
type: Jurisdiction
title: "Stafford County, KS"
classification: county
fips: "20185"
state: "KS"
demographics:
  population: 3978
  population_under_18: 968
  population_18_64: 2105
  population_65_plus: 905
  median_household_income: 64226
  poverty_rate: 10.49
  homeownership_rate: 82.33
  unemployment_rate: 2.49
  median_home_value: 97600
  gini_index: 0.4168
  vacancy_rate: 24.56
  race_white: 3370
  race_black: 8
  race_asian: 0
  race_native: 63
  hispanic: 533
  bachelors_plus: 892
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/113"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Stafford County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3978 |
| Under 18 | 968 |
| 18–64 | 2105 |
| 65+ | 905 |
| Median household income | 64226 |
| Poverty rate | 10.49 |
| Homeownership rate | 82.33 |
| Unemployment rate | 2.49 |
| Median home value | 97600 |
| Gini index | 0.4168 |
| Vacancy rate | 24.56 |
| White | 3370 |
| Black | 8 |
| Asian | 0 |
| Native | 63 |
| Hispanic/Latino | 533 |
| Bachelor's or higher | 892 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 113](/us/states/ks/districts/house/113.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
