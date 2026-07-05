---
type: Jurisdiction
title: "Ada County, ID"
classification: county
fips: "16001"
state: "ID"
demographics:
  population: 518935
  population_under_18: 114193
  population_18_64: 320472
  population_65_plus: 84270
  median_household_income: 91502
  poverty_rate: 8.34
  homeownership_rate: 70.8
  unemployment_rate: 3.14
  median_home_value: 512300
  gini_index: 0.4511
  vacancy_rate: 4.21
  race_white: 431302
  race_black: 6901
  race_asian: 14278
  race_native: 3444
  hispanic: 50948
  bachelors_plus: 215862
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.7626
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.2374
  - to: "us/states/id/districts/senate/23"
    rel: in-district
    area_weight: 0.5574
  - to: "us/states/id/districts/senate/18"
    rel: in-district
    area_weight: 0.1351
  - to: "us/states/id/districts/senate/19"
    rel: in-district
    area_weight: 0.0909
  - to: "us/states/id/districts/senate/14"
    rel: in-district
    area_weight: 0.081
  - to: "us/states/id/districts/senate/22"
    rel: in-district
    area_weight: 0.0379
  - to: "us/states/id/districts/senate/10"
    rel: in-district
    area_weight: 0.0221
  - to: "us/states/id/districts/senate/21"
    rel: in-district
    area_weight: 0.0197
  - to: "us/states/id/districts/senate/20"
    rel: in-district
    area_weight: 0.0169
  - to: "us/states/id/districts/senate/17"
    rel: in-district
    area_weight: 0.0134
  - to: "us/states/id/districts/senate/15"
    rel: in-district
    area_weight: 0.0127
  - to: "us/states/id/districts/senate/16"
    rel: in-district
    area_weight: 0.0125
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Ada County, ID

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 518935 |
| Under 18 | 114193 |
| 18–64 | 320472 |
| 65+ | 84270 |
| Median household income | 91502 |
| Poverty rate | 8.34 |
| Homeownership rate | 70.8 |
| Unemployment rate | 3.14 |
| Median home value | 512300 |
| Gini index | 0.4511 |
| Vacancy rate | 4.21 |
| White | 431302 |
| Black | 6901 |
| Asian | 14278 |
| Native | 3444 |
| Hispanic/Latino | 50948 |
| Bachelor's or higher | 215862 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 76% (congressional)
- [ID-02](/us/states/id/districts/02.md) — 24% (congressional)
- [ID Senate District 23](/us/states/id/districts/senate/23.md) — 56% (state senate)
- [ID Senate District 18](/us/states/id/districts/senate/18.md) — 14% (state senate)
- [ID Senate District 19](/us/states/id/districts/senate/19.md) — 9% (state senate)
- [ID Senate District 14](/us/states/id/districts/senate/14.md) — 8% (state senate)
- [ID Senate District 22](/us/states/id/districts/senate/22.md) — 4% (state senate)
- [ID Senate District 10](/us/states/id/districts/senate/10.md) — 2% (state senate)
- [ID Senate District 21](/us/states/id/districts/senate/21.md) — 2% (state senate)
- [ID Senate District 20](/us/states/id/districts/senate/20.md) — 2% (state senate)
- [ID Senate District 17](/us/states/id/districts/senate/17.md) — 1% (state senate)
- [ID Senate District 15](/us/states/id/districts/senate/15.md) — 1% (state senate)
- [ID Senate District 16](/us/states/id/districts/senate/16.md) — 1% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
