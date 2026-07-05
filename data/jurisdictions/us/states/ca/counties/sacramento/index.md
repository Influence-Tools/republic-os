---
type: Jurisdiction
title: "Sacramento County, CA"
classification: county
fips: "06067"
state: "CA"
demographics:
  population: 1594006
  population_under_18: 364525
  population_18_64: 986111
  population_65_plus: 243370
  median_household_income: 92175
  poverty_rate: 12.5
  homeownership_rate: 59.02
  unemployment_rate: 6.71
  median_home_value: 534200
  gini_index: 0.4443
  vacancy_rate: 4.57
  race_white: 708644
  race_black: 149365
  race_asian: 284307
  race_native: 16002
  hispanic: 385590
  bachelors_plus: 510269
districts:
  - to: "us/states/ca/districts/07"
    rel: in-district
    area_weight: 0.653
  - to: "us/states/ca/districts/06"
    rel: in-district
    area_weight: 0.2561
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.0885
  - to: "us/states/ca/districts/senate/6"
    rel: in-district
    area_weight: 0.5575
  - to: "us/states/ca/districts/senate/8"
    rel: in-district
    area_weight: 0.2742
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.1682
  - to: "us/states/ca/districts/house/9"
    rel: in-district
    area_weight: 0.5172
  - to: "us/states/ca/districts/house/7"
    rel: in-district
    area_weight: 0.1627
  - to: "us/states/ca/districts/house/6"
    rel: in-district
    area_weight: 0.1514
  - to: "us/states/ca/districts/house/10"
    rel: in-district
    area_weight: 0.117
  - to: "us/states/ca/districts/house/11"
    rel: in-district
    area_weight: 0.0516
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Sacramento County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1594006 |
| Under 18 | 364525 |
| 18–64 | 986111 |
| 65+ | 243370 |
| Median household income | 92175 |
| Poverty rate | 12.5 |
| Homeownership rate | 59.02 |
| Unemployment rate | 6.71 |
| Median home value | 534200 |
| Gini index | 0.4443 |
| Vacancy rate | 4.57 |
| White | 708644 |
| Black | 149365 |
| Asian | 284307 |
| Native | 16002 |
| Hispanic/Latino | 385590 |
| Bachelor's or higher | 510269 |

## Districts

- [CA-07](/us/states/ca/districts/07.md) — 65% (congressional)
- [CA-06](/us/states/ca/districts/06.md) — 26% (congressional)
- [CA-03](/us/states/ca/districts/03.md) — 9% (congressional)
- [CA Senate District 6](/us/states/ca/districts/senate/6.md) — 56% (state senate)
- [CA Senate District 8](/us/states/ca/districts/senate/8.md) — 27% (state senate)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 17% (state senate)
- [CA House District 9](/us/states/ca/districts/house/9.md) — 52% (state house)
- [CA House District 7](/us/states/ca/districts/house/7.md) — 16% (state house)
- [CA House District 6](/us/states/ca/districts/house/6.md) — 15% (state house)
- [CA House District 10](/us/states/ca/districts/house/10.md) — 12% (state house)
- [CA House District 11](/us/states/ca/districts/house/11.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
