---
type: Jurisdiction
title: "Rockingham County, NH"
classification: county
fips: "33015"
state: "NH"
demographics:
  population: 319082
  population_under_18: 58963
  population_18_64: 195093
  population_65_plus: 65026
  median_household_income: 118331
  poverty_rate: 4.77
  homeownership_rate: 78.45
  unemployment_rate: 3.55
  median_home_value: 497500
  gini_index: 0.4297
  vacancy_rate: 7.42
  race_white: 288970
  race_black: 2437
  race_asian: 6262
  race_native: 469
  hispanic: 11727
  bachelors_plus: 149644
districts:
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.7274
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.1856
  - to: "us/states/nh/districts/senate/23"
    rel: in-district
    area_weight: 0.2305
  - to: "us/states/nh/districts/senate/17"
    rel: in-district
    area_weight: 0.1648
  - to: "us/states/nh/districts/senate/24"
    rel: in-district
    area_weight: 0.1292
  - to: "us/states/nh/districts/senate/19"
    rel: in-district
    area_weight: 0.0981
  - to: "us/states/nh/districts/senate/14"
    rel: in-district
    area_weight: 0.0891
  - to: "us/states/nh/districts/senate/16"
    rel: in-district
    area_weight: 0.0758
  - to: "us/states/nh/districts/senate/21"
    rel: in-district
    area_weight: 0.0661
  - to: "us/states/nh/districts/senate/22"
    rel: in-district
    area_weight: 0.0599
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Rockingham County, NH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 319082 |
| Under 18 | 58963 |
| 18–64 | 195093 |
| 65+ | 65026 |
| Median household income | 118331 |
| Poverty rate | 4.77 |
| Homeownership rate | 78.45 |
| Unemployment rate | 3.55 |
| Median home value | 497500 |
| Gini index | 0.4297 |
| Vacancy rate | 7.42 |
| White | 288970 |
| Black | 2437 |
| Asian | 6262 |
| Native | 469 |
| Hispanic/Latino | 11727 |
| Bachelor's or higher | 149644 |

## Districts

- [NH-01](/us/states/nh/districts/01.md) — 73% (congressional)
- [NH-02](/us/states/nh/districts/02.md) — 19% (congressional)
- [NH Senate District 23](/us/states/nh/districts/senate/23.md) — 23% (state senate)
- [NH Senate District 17](/us/states/nh/districts/senate/17.md) — 16% (state senate)
- [NH Senate District 24](/us/states/nh/districts/senate/24.md) — 13% (state senate)
- [NH Senate District 19](/us/states/nh/districts/senate/19.md) — 10% (state senate)
- [NH Senate District 14](/us/states/nh/districts/senate/14.md) — 9% (state senate)
- [NH Senate District 16](/us/states/nh/districts/senate/16.md) — 8% (state senate)
- [NH Senate District 21](/us/states/nh/districts/senate/21.md) — 7% (state senate)
- [NH Senate District 22](/us/states/nh/districts/senate/22.md) — 6% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
