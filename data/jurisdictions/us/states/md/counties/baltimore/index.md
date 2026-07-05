---
type: Jurisdiction
title: "Baltimore County, MD"
classification: county
fips: "24005"
state: "MD"
demographics:
  population: 850796
  population_under_18: 185984
  population_18_64: 510443
  population_65_plus: 154369
  median_household_income: 91768
  poverty_rate: 9.78
  homeownership_rate: 66.38
  unemployment_rate: 4.89
  median_home_value: 349300
  gini_index: 0.458
  vacancy_rate: 5.14
  race_white: 447437
  race_black: 260785
  race_asian: 52203
  race_native: 2363
  hispanic: 66062
  bachelors_plus: 361826
districts:
  - to: "us/states/md/districts/02"
    rel: in-district
    area_weight: 0.6171
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.2142
  - to: "us/states/md/districts/07"
    rel: in-district
    area_weight: 0.0928
  - to: "us/states/md/districts/senate/42"
    rel: in-district
    area_weight: 0.3575
  - to: "us/states/md/districts/senate/10"
    rel: in-district
    area_weight: 0.1474
  - to: "us/states/md/districts/senate/7"
    rel: in-district
    area_weight: 0.1293
  - to: "us/states/md/districts/senate/11"
    rel: in-district
    area_weight: 0.1073
  - to: "us/states/md/districts/senate/6"
    rel: in-district
    area_weight: 0.0768
  - to: "us/states/md/districts/senate/44"
    rel: in-district
    area_weight: 0.0434
  - to: "us/states/md/districts/senate/8"
    rel: in-district
    area_weight: 0.0395
  - to: "us/states/md/districts/senate/43"
    rel: in-district
    area_weight: 0.0091
  - to: "us/states/md/districts/house/42a"
    rel: in-district
    area_weight: 0.3354
  - to: "us/states/md/districts/house/10"
    rel: in-district
    area_weight: 0.1474
  - to: "us/states/md/districts/house/7a"
    rel: in-district
    area_weight: 0.1291
  - to: "us/states/md/districts/house/6"
    rel: in-district
    area_weight: 0.0768
  - to: "us/states/md/districts/house/11b"
    rel: in-district
    area_weight: 0.0738
  - to: "us/states/md/districts/house/8"
    rel: in-district
    area_weight: 0.0395
  - to: "us/states/md/districts/house/11a"
    rel: in-district
    area_weight: 0.0335
  - to: "us/states/md/districts/house/44b"
    rel: in-district
    area_weight: 0.0312
  - to: "us/states/md/districts/house/42b"
    rel: in-district
    area_weight: 0.0221
  - to: "us/states/md/districts/house/44a"
    rel: in-district
    area_weight: 0.0122
  - to: "us/states/md/districts/house/43b"
    rel: in-district
    area_weight: 0.0091
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Baltimore County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 850796 |
| Under 18 | 185984 |
| 18–64 | 510443 |
| 65+ | 154369 |
| Median household income | 91768 |
| Poverty rate | 9.78 |
| Homeownership rate | 66.38 |
| Unemployment rate | 4.89 |
| Median home value | 349300 |
| Gini index | 0.458 |
| Vacancy rate | 5.14 |
| White | 447437 |
| Black | 260785 |
| Asian | 52203 |
| Native | 2363 |
| Hispanic/Latino | 66062 |
| Bachelor's or higher | 361826 |

## Districts

- [MD-02](/us/states/md/districts/02.md) — 62% (congressional)
- [MD-01](/us/states/md/districts/01.md) — 21% (congressional)
- [MD-07](/us/states/md/districts/07.md) — 9% (congressional)
- [MD Senate District 42](/us/states/md/districts/senate/42.md) — 36% (state senate)
- [MD Senate District 10](/us/states/md/districts/senate/10.md) — 15% (state senate)
- [MD Senate District 7](/us/states/md/districts/senate/7.md) — 13% (state senate)
- [MD Senate District 11](/us/states/md/districts/senate/11.md) — 11% (state senate)
- [MD Senate District 6](/us/states/md/districts/senate/6.md) — 8% (state senate)
- [MD Senate District 44](/us/states/md/districts/senate/44.md) — 4% (state senate)
- [MD Senate District 8](/us/states/md/districts/senate/8.md) — 4% (state senate)
- [MD Senate District 43](/us/states/md/districts/senate/43.md) — 1% (state senate)
- [MD House District 42A](/us/states/md/districts/house/42a.md) — 34% (state house)
- [MD House District 10](/us/states/md/districts/house/10.md) — 15% (state house)
- [MD House District 7A](/us/states/md/districts/house/7a.md) — 13% (state house)
- [MD House District 6](/us/states/md/districts/house/6.md) — 8% (state house)
- [MD House District 11B](/us/states/md/districts/house/11b.md) — 7% (state house)
- [MD House District 8](/us/states/md/districts/house/8.md) — 4% (state house)
- [MD House District 11A](/us/states/md/districts/house/11a.md) — 3% (state house)
- [MD House District 44B](/us/states/md/districts/house/44b.md) — 3% (state house)
- [MD House District 42B](/us/states/md/districts/house/42b.md) — 2% (state house)
- [MD House District 44A](/us/states/md/districts/house/44a.md) — 1% (state house)
- [MD House District 43B](/us/states/md/districts/house/43b.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
