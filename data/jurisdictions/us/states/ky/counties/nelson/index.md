---
type: Jurisdiction
title: "Nelson County, KY"
classification: county
fips: "21179"
state: "KY"
demographics:
  population: 47606
  population_under_18: 10972
  population_18_64: 28343
  population_65_plus: 8291
  median_household_income: 69562
  poverty_rate: 10.85
  homeownership_rate: 78.33
  unemployment_rate: 3.33
  median_home_value: 238000
  gini_index: 0.4315
  vacancy_rate: 5.8
  race_white: 42741
  race_black: 2535
  race_asian: 236
  race_native: 26
  hispanic: 1397
  bachelors_plus: 10966
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.5076
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.4875
  - to: "us/states/ky/districts/senate/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/50"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Nelson County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47606 |
| Under 18 | 10972 |
| 18–64 | 28343 |
| 65+ | 8291 |
| Median household income | 69562 |
| Poverty rate | 10.85 |
| Homeownership rate | 78.33 |
| Unemployment rate | 3.33 |
| Median home value | 238000 |
| Gini index | 0.4315 |
| Vacancy rate | 5.8 |
| White | 42741 |
| Black | 2535 |
| Asian | 236 |
| Native | 26 |
| Hispanic/Latino | 1397 |
| Bachelor's or higher | 10966 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 51% (congressional)
- [KY-04](/us/states/ky/districts/04.md) — 49% (congressional)
- [KY Senate District 14](/us/states/ky/districts/senate/14.md) — 100% (state senate)
- [KY House District 50](/us/states/ky/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
