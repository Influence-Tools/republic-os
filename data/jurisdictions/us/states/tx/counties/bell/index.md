---
type: Jurisdiction
title: "Bell County, TX"
classification: county
fips: "48027"
state: "TX"
demographics:
  population: 386897
  population_under_18: 106248
  population_18_64: 234502
  population_65_plus: 46147
  median_household_income: 68865
  poverty_rate: 14.5
  homeownership_rate: 56.51
  unemployment_rate: 6.77
  median_home_value: 241000
  gini_index: 0.4532
  vacancy_rate: 8.2
  race_white: 190153
  race_black: 88557
  race_asian: 11766
  race_native: 3317
  hispanic: 101713
  bachelors_plus: 86658
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.8349
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.165
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/54"
    rel: in-district
    area_weight: 0.8062
  - to: "us/states/tx/districts/house/55"
    rel: in-district
    area_weight: 0.1936
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bell County, TX

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 386897 |
| Under 18 | 106248 |
| 18–64 | 234502 |
| 65+ | 46147 |
| Median household income | 68865 |
| Poverty rate | 14.5 |
| Homeownership rate | 56.51 |
| Unemployment rate | 6.77 |
| Median home value | 241000 |
| Gini index | 0.4532 |
| Vacancy rate | 8.2 |
| White | 190153 |
| Black | 88557 |
| Asian | 11766 |
| Native | 3317 |
| Hispanic/Latino | 101713 |
| Bachelor's or higher | 86658 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 83% (congressional)
- [TX-11](/us/states/tx/districts/11.md) — 16% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 54](/us/states/tx/districts/house/54.md) — 81% (state house)
- [TX House District 55](/us/states/tx/districts/house/55.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
