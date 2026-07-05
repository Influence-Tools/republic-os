---
type: Jurisdiction
title: "Washington County, UT"
classification: county
fips: "49053"
state: "UT"
demographics:
  population: 196431
  population_under_18: 48021
  population_18_64: 104607
  population_65_plus: 43803
  median_household_income: 80632
  poverty_rate: 9.84
  homeownership_rate: 71.64
  unemployment_rate: 3.6
  median_home_value: 510700
  gini_index: 0.4431
  vacancy_rate: 15.09
  race_white: 166345
  race_black: 853
  race_asian: 2314
  race_native: 1524
  hispanic: 23790
  bachelors_plus: 62615
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ut/districts/senate/29"
    rel: in-district
    area_weight: 0.5375
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.3355
  - to: "us/states/ut/districts/senate/28"
    rel: in-district
    area_weight: 0.1268
  - to: "us/states/ut/districts/house/72"
    rel: in-district
    area_weight: 0.4064
  - to: "us/states/ut/districts/house/75"
    rel: in-district
    area_weight: 0.3565
  - to: "us/states/ut/districts/house/74"
    rel: in-district
    area_weight: 0.1749
  - to: "us/states/ut/districts/house/73"
    rel: in-district
    area_weight: 0.062
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Washington County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 196431 |
| Under 18 | 48021 |
| 18–64 | 104607 |
| 65+ | 43803 |
| Median household income | 80632 |
| Poverty rate | 9.84 |
| Homeownership rate | 71.64 |
| Unemployment rate | 3.6 |
| Median home value | 510700 |
| Gini index | 0.4431 |
| Vacancy rate | 15.09 |
| White | 166345 |
| Black | 853 |
| Asian | 2314 |
| Native | 1524 |
| Hispanic/Latino | 23790 |
| Bachelor's or higher | 62615 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 29](/us/states/ut/districts/senate/29.md) — 54% (state senate)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 34% (state senate)
- [UT Senate District 28](/us/states/ut/districts/senate/28.md) — 13% (state senate)
- [UT House District 72](/us/states/ut/districts/house/72.md) — 41% (state house)
- [UT House District 75](/us/states/ut/districts/house/75.md) — 36% (state house)
- [UT House District 74](/us/states/ut/districts/house/74.md) — 17% (state house)
- [UT House District 73](/us/states/ut/districts/house/73.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
