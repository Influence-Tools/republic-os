---
type: Jurisdiction
title: "Independence County, AR"
classification: county
fips: "05063"
state: "AR"
demographics:
  population: 38175
  population_under_18: 9283
  population_18_64: 22184
  population_65_plus: 6708
  median_household_income: 56609
  poverty_rate: 20.39
  homeownership_rate: 69.19
  unemployment_rate: 3.88
  median_home_value: 142600
  gini_index: 0.4854
  vacancy_rate: 12.8
  race_white: 31927
  race_black: 701
  race_asian: 332
  race_native: 228
  hispanic: 3382
  bachelors_plus: 6119
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/28"
    rel: in-district
    area_weight: 0.5006
  - to: "us/states/ar/districts/house/40"
    rel: in-district
    area_weight: 0.2953
  - to: "us/states/ar/districts/house/39"
    rel: in-district
    area_weight: 0.204
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Independence County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38175 |
| Under 18 | 9283 |
| 18–64 | 22184 |
| 65+ | 6708 |
| Median household income | 56609 |
| Poverty rate | 20.39 |
| Homeownership rate | 69.19 |
| Unemployment rate | 3.88 |
| Median home value | 142600 |
| Gini index | 0.4854 |
| Vacancy rate | 12.8 |
| White | 31927 |
| Black | 701 |
| Asian | 332 |
| Native | 228 |
| Hispanic/Latino | 3382 |
| Bachelor's or higher | 6119 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 100% (state senate)
- [AR House District 28](/us/states/ar/districts/house/28.md) — 50% (state house)
- [AR House District 40](/us/states/ar/districts/house/40.md) — 30% (state house)
- [AR House District 39](/us/states/ar/districts/house/39.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
