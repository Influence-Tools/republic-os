---
type: Jurisdiction
title: "Carson City, NV"
classification: county
fips: "32510"
state: "NV"
demographics:
  population: 58384
  population_under_18: 11633
  population_18_64: 34368
  population_65_plus: 12383
  median_household_income: 72355
  poverty_rate: 10.34
  homeownership_rate: 62.34
  unemployment_rate: 5.51
  median_home_value: 453000
  gini_index: 0.4529
  vacancy_rate: 5.82
  race_white: 39667
  race_black: 1037
  race_asian: 1468
  race_native: 1267
  hispanic: 15385
  bachelors_plus: 13886
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/senate/16"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nv/districts/house/40"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Carson City, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58384 |
| Under 18 | 11633 |
| 18–64 | 34368 |
| 65+ | 12383 |
| Median household income | 72355 |
| Poverty rate | 10.34 |
| Homeownership rate | 62.34 |
| Unemployment rate | 5.51 |
| Median home value | 453000 |
| Gini index | 0.4529 |
| Vacancy rate | 5.82 |
| White | 39667 |
| Black | 1037 |
| Asian | 1468 |
| Native | 1267 |
| Hispanic/Latino | 15385 |
| Bachelor's or higher | 13886 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 16](/us/states/nv/districts/senate/16.md) — 100% (state senate)
- [NV House District 40](/us/states/nv/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
