---
type: Jurisdiction
title: "Cleburne County, AR"
classification: county
fips: "05023"
state: "AR"
demographics:
  population: 25226
  population_under_18: 4813
  population_18_64: 13503
  population_65_plus: 6910
  median_household_income: 55798
  poverty_rate: 13.88
  homeownership_rate: 80.59
  unemployment_rate: 6.43
  median_home_value: 179800
  gini_index: 0.4565
  vacancy_rate: 32.84
  race_white: 23651
  race_black: 73
  race_asian: 50
  race_native: 123
  hispanic: 747
  bachelors_plus: 4726
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.5293
  - to: "us/states/ar/districts/senate/18"
    rel: in-district
    area_weight: 0.2899
  - to: "us/states/ar/districts/senate/24"
    rel: in-district
    area_weight: 0.1808
  - to: "us/states/ar/districts/house/41"
    rel: in-district
    area_weight: 0.8904
  - to: "us/states/ar/districts/house/40"
    rel: in-district
    area_weight: 0.081
  - to: "us/states/ar/districts/house/42"
    rel: in-district
    area_weight: 0.0286
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Cleburne County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25226 |
| Under 18 | 4813 |
| 18–64 | 13503 |
| 65+ | 6910 |
| Median household income | 55798 |
| Poverty rate | 13.88 |
| Homeownership rate | 80.59 |
| Unemployment rate | 6.43 |
| Median home value | 179800 |
| Gini index | 0.4565 |
| Vacancy rate | 32.84 |
| White | 23651 |
| Black | 73 |
| Asian | 50 |
| Native | 123 |
| Hispanic/Latino | 747 |
| Bachelor's or higher | 4726 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 53% (state senate)
- [AR Senate District 18](/us/states/ar/districts/senate/18.md) — 29% (state senate)
- [AR Senate District 24](/us/states/ar/districts/senate/24.md) — 18% (state senate)
- [AR House District 41](/us/states/ar/districts/house/41.md) — 89% (state house)
- [AR House District 40](/us/states/ar/districts/house/40.md) — 8% (state house)
- [AR House District 42](/us/states/ar/districts/house/42.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
