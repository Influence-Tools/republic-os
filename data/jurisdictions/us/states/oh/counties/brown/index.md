---
type: Jurisdiction
title: "Brown County, OH"
classification: county
fips: "39015"
state: "OH"
demographics:
  population: 43845
  population_under_18: 9983
  population_18_64: 25470
  population_65_plus: 8392
  median_household_income: 71270
  poverty_rate: 19.6
  homeownership_rate: 77.18
  unemployment_rate: 4.93
  median_home_value: 196200
  gini_index: 0.4532
  vacancy_rate: 12.4
  race_white: 41754
  race_black: 298
  race_asian: 131
  race_native: 13
  hispanic: 572
  bachelors_plus: 6387
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/14"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/house/63"
    rel: in-district
    area_weight: 0.5429
  - to: "us/states/oh/districts/house/90"
    rel: in-district
    area_weight: 0.4567
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Brown County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43845 |
| Under 18 | 9983 |
| 18–64 | 25470 |
| 65+ | 8392 |
| Median household income | 71270 |
| Poverty rate | 19.6 |
| Homeownership rate | 77.18 |
| Unemployment rate | 4.93 |
| Median home value | 196200 |
| Gini index | 0.4532 |
| Vacancy rate | 12.4 |
| White | 41754 |
| Black | 298 |
| Asian | 131 |
| Native | 13 |
| Hispanic/Latino | 572 |
| Bachelor's or higher | 6387 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 14](/us/states/oh/districts/senate/14.md) — 100% (state senate)
- [OH House District 63](/us/states/oh/districts/house/63.md) — 54% (state house)
- [OH House District 90](/us/states/oh/districts/house/90.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
