---
type: Jurisdiction
title: "Starr County, TX"
classification: county
fips: "48427"
state: "TX"
demographics:
  population: 66067
  population_under_18: 21472
  population_18_64: 37076
  population_65_plus: 7519
  median_household_income: 37639
  poverty_rate: 33.52
  homeownership_rate: 69.53
  unemployment_rate: 10.44
  median_home_value: 95100
  gini_index: 0.5335
  vacancy_rate: 17.21
  race_white: 21731
  race_black: 280
  race_asian: 38
  race_native: 90
  hispanic: 64218
  bachelors_plus: 6793
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Starr County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66067 |
| Under 18 | 21472 |
| 18–64 | 37076 |
| 65+ | 7519 |
| Median household income | 37639 |
| Poverty rate | 33.52 |
| Homeownership rate | 69.53 |
| Unemployment rate | 10.44 |
| Median home value | 95100 |
| Gini index | 0.5335 |
| Vacancy rate | 17.21 |
| White | 21731 |
| Black | 280 |
| Asian | 38 |
| Native | 90 |
| Hispanic/Latino | 64218 |
| Bachelor's or higher | 6793 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
