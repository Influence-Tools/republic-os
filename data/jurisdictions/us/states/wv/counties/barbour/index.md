---
type: Jurisdiction
title: "Barbour County, WV"
classification: county
fips: "54001"
state: "WV"
demographics:
  population: 15424
  population_under_18: 3072
  population_18_64: 9096
  population_65_plus: 3256
  median_household_income: 51394
  poverty_rate: 19.98
  homeownership_rate: 78.33
  unemployment_rate: 8.49
  median_home_value: 131900
  gini_index: 0.4444
  vacancy_rate: 13.64
  race_white: 13963
  race_black: 234
  race_asian: 47
  race_native: 35
  hispanic: 192
  bachelors_plus: 1762
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/house/68"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Barbour County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15424 |
| Under 18 | 3072 |
| 18–64 | 9096 |
| 65+ | 3256 |
| Median household income | 51394 |
| Poverty rate | 19.98 |
| Homeownership rate | 78.33 |
| Unemployment rate | 8.49 |
| Median home value | 131900 |
| Gini index | 0.4444 |
| Vacancy rate | 13.64 |
| White | 13963 |
| Black | 234 |
| Asian | 47 |
| Native | 35 |
| Hispanic/Latino | 192 |
| Bachelor's or higher | 1762 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 68](/us/states/wv/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
