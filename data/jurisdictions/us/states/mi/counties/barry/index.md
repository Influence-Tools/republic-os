---
type: Jurisdiction
title: "Barry County, MI"
classification: county
fips: "26015"
state: "MI"
demographics:
  population: 63409
  population_under_18: 13753
  population_18_64: 37284
  population_65_plus: 12372
  median_household_income: 77500
  poverty_rate: 8.41
  homeownership_rate: 87.31
  unemployment_rate: 4.3
  median_home_value: 264100
  gini_index: 0.4468
  vacancy_rate: 11.88
  race_white: 58772
  race_black: 214
  race_asian: 379
  race_native: 176
  hispanic: 2337
  bachelors_plus: 14741
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/43"
    rel: in-district
    area_weight: 0.4387
  - to: "us/states/mi/districts/house/78"
    rel: in-district
    area_weight: 0.3737
  - to: "us/states/mi/districts/house/79"
    rel: in-district
    area_weight: 0.1876
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Barry County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 63409 |
| Under 18 | 13753 |
| 18–64 | 37284 |
| 65+ | 12372 |
| Median household income | 77500 |
| Poverty rate | 8.41 |
| Homeownership rate | 87.31 |
| Unemployment rate | 4.3 |
| Median home value | 264100 |
| Gini index | 0.4468 |
| Vacancy rate | 11.88 |
| White | 58772 |
| Black | 214 |
| Asian | 379 |
| Native | 176 |
| Hispanic/Latino | 2337 |
| Bachelor's or higher | 14741 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 18](/us/states/mi/districts/senate/18.md) — 100% (state senate)
- [MI House District 43](/us/states/mi/districts/house/43.md) — 44% (state house)
- [MI House District 78](/us/states/mi/districts/house/78.md) — 37% (state house)
- [MI House District 79](/us/states/mi/districts/house/79.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
