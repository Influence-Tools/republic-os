---
type: Jurisdiction
title: "Johnson County, TX"
classification: county
fips: "48251"
state: "TX"
demographics:
  population: 195597
  population_under_18: 50259
  population_18_64: 117902
  population_65_plus: 27436
  median_household_income: 84859
  poverty_rate: 10.0
  homeownership_rate: 74.65
  unemployment_rate: 3.62
  median_home_value: 285900
  gini_index: 0.4129
  vacancy_rate: 7.47
  race_white: 140616
  race_black: 10634
  race_asian: 2396
  race_native: 1532
  hispanic: 49502
  bachelors_plus: 41916
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.68
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.3192
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/58"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Johnson County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 195597 |
| Under 18 | 50259 |
| 18–64 | 117902 |
| 65+ | 27436 |
| Median household income | 84859 |
| Poverty rate | 10.0 |
| Homeownership rate | 74.65 |
| Unemployment rate | 3.62 |
| Median home value | 285900 |
| Gini index | 0.4129 |
| Vacancy rate | 7.47 |
| White | 140616 |
| Black | 10634 |
| Asian | 2396 |
| Native | 1532 |
| Hispanic/Latino | 49502 |
| Bachelor's or higher | 41916 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 68% (congressional)
- [TX-06](/us/states/tx/districts/06.md) — 32% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 58](/us/states/tx/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
