---
type: Jurisdiction
title: "Lee County, TX"
classification: county
fips: "48287"
state: "TX"
demographics:
  population: 17971
  population_under_18: 3824
  population_18_64: 10569
  population_65_plus: 3578
  median_household_income: 76371
  poverty_rate: 11.33
  homeownership_rate: 77.81
  unemployment_rate: 6.51
  median_home_value: 267800
  gini_index: 0.4069
  vacancy_rate: 12.49
  race_white: 11832
  race_black: 1731
  race_asian: 47
  race_native: 353
  hispanic: 4774
  bachelors_plus: 3225
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/17"
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

# Lee County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17971 |
| Under 18 | 3824 |
| 18–64 | 10569 |
| 65+ | 3578 |
| Median household income | 76371 |
| Poverty rate | 11.33 |
| Homeownership rate | 77.81 |
| Unemployment rate | 6.51 |
| Median home value | 267800 |
| Gini index | 0.4069 |
| Vacancy rate | 12.49 |
| White | 11832 |
| Black | 1731 |
| Asian | 47 |
| Native | 353 |
| Hispanic/Latino | 4774 |
| Bachelor's or higher | 3225 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 17](/us/states/tx/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
